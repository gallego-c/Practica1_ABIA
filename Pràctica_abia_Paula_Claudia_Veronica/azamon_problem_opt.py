from typing import Generator
from aima.search import Problem
from azamon_operators import AzamonOperator
from azamon_state_opt import StateRepresentation

class AzamonProblem(Problem):
    def __init__(self, initial_state: StateRepresentation, maximize_happiness: bool = False, mode_simulated_annealing: bool = False, combine_heuristic: bool = False, alpha: float = 0.1, op1=True, op2=True, op3=False):
        self.maximize_happiness = maximize_happiness
        self.mode_simulated_annealing = mode_simulated_annealing
        self.combine_heuristic = combine_heuristic
        self.alpha = alpha
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3self.costs = []
        self.iteration = 0

        # self.costs = []
        # self.iteration = 0
        
        super().__init__(initial_state)

    def actions(self, state: StateRepresentation) -> Generator[AzamonOperator, None, None]:
        return state.generate_actions_automatic(self.mode_simulated_annealing, self.op1, self.op2, self.op3)
    
    def result(self, state: StateRepresentation, action: AzamonOperator) -> StateRepresentation:
    ## Opcion con cost_tracking ##
        # new_state = state.apply_action(action)
        # self.costs.append(abs(self.value(new_state)))
        # self.iteration += 1
        # return new_state
        return state.apply_action(action)

    def value(self, state: StateRepresentation) -> float:
        # Heurística combinada con ponderaciones
        if self.maximize_happiness:
            return state.heuristic_happiness()  # Maximizar solo la felicidad
        elif self.combine_heuristic:
            return -state.heuristic_cost_happy(self.alpha)
        else:
            return -state.heuristic_cost() # Minimizar solo el coste

    def goal_test(self, state: StateRepresentation) -> bool:
        return False

## Opcion con cost_tracking ##
    # def cost_tracking(self) -> float:
    #     filename = 'costs.csv'
    #     with open(filename, 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(['Iteration', 'Cost', 'Happiness'])
    #         for i in range(len(self.costs)):
    #             writer.writerow([i, self.costs[i]])
