#!/usr/bin/env python3
from tngrokking.torchmps.trainer.cli import CellularAutomataTrainerCLI

if __name__ == '__main__':
    ca = CellularAutomataTrainerCLI()
    ca.train()
