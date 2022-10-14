"""Handle reporting events."""
from abc import ABC, abstractmethod
from population import PopulationBase

class ReporterBase(ABC):
    @abstractmethod
    def new_evolution(population: PopulationBase, clean_reporter: bool) -> None:
        pass
    
    @abstractmethod
    def new_revolution(population: PopulationBase, revolution: int) -> None:
        pass
    
    @abstractmethod
    def reproduced(population: PopulationBase) -> None:
        pass
    
    @abstractmethod
    def evaluated(population: PopulationBase) -> None:
        pass
    
    @abstractmethod
    def end_revolution(population: PopulationBase) -> None:
        pass
    
    @abstractmethod
    def end_evolution(population: PopulationBase) -> None:
        pass