"""Population handler"""
from typing import Callable

from genome import GenomeBase

class PopulationBase(object):
    def __init__(self
                 ,genome_cls: Callable[..., GenomeBase]
                 ) -> None:
        self.genome_cls = genome_cls
    
    
    def reproduce(self) -> None:
        pass
    
    def speciate(self) -> None:
        pass
    
    def eval_fitness(self, fitness_func: Callable[['PopulationBase'], None]) -> None:
        pass

