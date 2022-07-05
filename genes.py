# standard libs
from random import randrange, uniform

# external libs

# internal imports


class Gene():
    # x = 0
    # y = 0
    genomes = ['x', 'y']
    score = 0

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({},{})\ts{}'.format(self.x, self.y, self.score)

    # methods for comparison with a regular int or float:
    def __eq__(self, other):
        return AssertionError("can't compare floats scores with equality")

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __le__(self, other):
        return self.score <= other.score

    def shuffle_genomes(self, downRange=-99999, upperRagne=99999):
        """Randomly shuffle the genomes of a gene

        Args:
            downRange (int): The lower number possible for the randomness. Defaults to -99999.
            upperRagne (int): The upper number possible for the randomness. Defaults to 99999.
        """
        for genome in self.genomes:
            setattr(self, genome, randrange(downRange, upperRagne))

    def clone(self):
        """Clone the given genome into a new one

        Args:
            gene (Gene): The gene to be cloned

        Returns:
            Gene: A brend new Gene equal to the given one
        """

        new_gene = Gene(self.x, self.y)
        new_gene.score = self.score
        return new_gene

    def mutate(self, chance: int, sample_space: int, magnitude_max: int, allow_multiple_mutations: bool):
        """Make a new mutated gene based on the given one

        Args:
            chance (int): how many chances in sample_space for a to genome mutate
            sample_space (int): what's the total space of probability for mutations
            magnitude_max (int): how big can the mutation possibly be
            allow_multiple_mutations (bool): if True, more than one genome can mutate at a time

        Returns:
            int: how many mutations happend
        """
        mutation_counter = 0

        # mutate each gene
        for genome in self.genomes:
            coin = randrange(sample_space)
            if(coin >= chance):
                if(allow_multiple_mutations):
                    continue
                else:
                    return mutation_counter

            # calculate and apply mutation
            mutation_magnitude = uniform(magnitude_max, magnitude_max + 1)
            setattr(self, genome, getattr(self, genome) + mutation_magnitude)

            # stop if multiple mutations are not allower
            if(not allow_multiple_mutations):
                break

        return mutation_counter
