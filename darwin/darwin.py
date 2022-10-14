"""Evolution engine."""

from ast import Try
from typing import Callable
from genome import GenomeBase
from reporter import ReporterBase
from population import PopulationBase

class ExceptionTermination(Exception):
    pass


class Darwin(object):
    def __init__(self
                 ,fitness_func: Callable[[PopulationBase], None]
                 ,reporter: ReporterBase
                 ,population: PopulationBase
                 ) -> None:
        self.fitness_func: Callable[[GenomeBase], float] = fitness_func
        self.reporter: ReporterBase = reporter
        self.population: PopulationBase = population
        
    def eval_fitness(self) -> None:
        pass

    def eval_termination(self) -> None:
        pass
    
    def new_revolution(self, revolution_number:int = 0) -> None:
        """
        Execute one full revolution of the population. 
        It compreend the steps:
            + Reproduction of population: if first revolution all population will 
            be created.
            + Eval fitness of population.
            + Speciate: where is defined the species, survival individuals(elites)
            and the parents pool from which will be chosen the parents of the new
            generation
        It also execute all reporters events.

        Args:
            revolution_number (int, optional): _description_. Defaults to 0.
        """
        self.reporter.new_revolution(self.population, revolution_number)
        self.population.reproduce()
        self.reporter.reproduced(self.population)
        self.eval_fitness()
        self.reporter.evaluated(self.population)
        self.population.speciate()
        self.reporter.end_revolution(self.population)
    
    def evolve(self
               ,n:int = 100
               ,clean_reporter: bool = True) -> None:
        self.reporter.new_evolution(self.population, clean_reporter)
        try:
            for i in range(n):
                self.new_revolution(i)
                self.eval_termination()
        except ExceptionTermination:
            pass      
        self.reporter.end_evolution(self.population)
    
        
            
