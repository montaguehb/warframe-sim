from random import choices, randint
import time
import numpy, matplotlib.pyplot
import csv


class Sim:
    def __init__(
        self,
        drop_table: list[str],
        prob_table: list[float],
        parts: dict,
        required_tokens: int,
    ):
        self.drop_table = drop_table
        self.prob_table = prob_table
        self.parts = parts
        self.required_tokens = required_tokens
        self.tokens = 0
        self.drops = []
        self.sims = []

    def disruption_sim(self) -> int:
        drops = []
        runs = 0
        current_run_tokens = self.required_tokens
        while (not all(n in drops for n in self.parts.items())) and (
            current_run_tokens >= 0
        ):
            runs += 1
            drop = choices(self.drop_table, self.prob_table)
            current_run_tokens -= randint(5, 7)
            if drop not in drops:
                current_run_tokens -= dante_parts.get(drop[0], 0)
            drops.append(drop)
        return runs

    def total_sim(self, num_runs: int) -> list[int]:
        runs = []
        for _ in range(0, num_runs):
            runs.append(self.disruption_sim())
        self.sims.append(runs)
        return runs

    def save_sim(self, sim: list[int], file_name: str) -> None:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        numpy.savetxt(f'{file_name}-{timestr}.csv', sim, delimiter=", ", fmt="% s")

    def show_sim(self, sim: list[int]) -> None:
        matplotlib.pyplot.hist(sim, bins=range(0, 50), density=False)
        matplotlib.pyplot.title("Test")
        matplotlib.pyplot.show()


rot_c_drop_table = [
    "endo",
    "relics",
    "Dante Blueprint",
    "Dante Chassis",
    "Dantee Neuroptics",
    "Dantee Systems",
]
rot_c_prob = [0.175, 0.6, 0.075, 0.05, 0.05, 0.05]
dante_parts = {
    "Dante Blueprint": 270,
    "Dante Chassis": 90,
    "Dantee Neuroptics": 90,
    "Dantee Systems": 90,
}
vessel_cappilaries = 540

dante = Sim(rot_c_drop_table, rot_c_prob, dante_parts, vessel_cappilaries)
dante.total_sim(1000)
dante.save_sim(dante.sims[0], "Dante_sim")
dante.show_sim(dante.sims[0])