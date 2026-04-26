from src.backtracking_solver import BacktrackingSolver


class SolverFactory:
    @staticmethod
    def create_solver(solver_type):
        if solver_type == "backtracking":
            return BacktrackingSolver()

        raise ValueError(f"Unsupported solver type: {solver_type}")