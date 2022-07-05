# standard libs

# external libs

# internal imports
from random import randrange
from genes import Gene


def main():
    # pop == population
    pop_size = 1000
    pop = []
    gen_counter = 0
    gen_max = 100
    classif_threshold = 0.1
    exploration = 0.02
    chance = 1
    sample_space = 1000
    magnitude_max = 0.15
    allow_multiple_mutations = True

    # how many good individual are gonna be selected at each generation
    threshold = int((classif_threshold - exploration) * pop_size)

    # how mnay week individual are gonna be selected at each generation
    week_threshold = int(exploration * pop_size)

    # init population
    for _ in range(pop_size):
        gene = Gene()
        gene.shuffle_genomes()
        pop.append(gene)

    while gen_counter < gen_max:
        pop_classify(pop)
        gen_counter += 1

        # selecting the best individuals
        pop_selection = pop[:threshold]

        # exploring with less adapted individuals
        for _ in range(week_threshold):
            pick = randrange(threshold, pop_size)
            pop_selection.append(pop[pick])

        # reproducing the genes
        pop_len = len(pop)
        pop_selection_len = len(pop_selection)
        pop_new = [gene for gene in pop_selection]
        reproducer = 0
        while len(pop_new) < pop_len:
            child: Gene = pop_selection[reproducer].clone()
            child.mutate(chance, sample_space, magnitude_max, allow_multiple_mutations)
            pop_new.append(child)

            # reproduce next gene
            reproducer += 1
            if(reproducer >= pop_selection_len):
                reproducer = 0
        pop = pop_new

        # show progress
        print('gen-{} -> {}'.format(gen_counter, pop[-1]))

    pop_classify(pop)
    # print_population(pop)


def print_population(pop):
    """Transforme the entire genetic population into a printable string

    Args:
        pop (Gene[]): _description_
    """
    for gene in pop:
        print(gene)


def pop_classify(pop):
    """Classify the entire gene population

    Args:
        pop (Gene[]): The population to be classified
    """
    # calc score
    for gene in pop:
        gene.score = abs(optmize_me(gene.x, gene.y))
    pop.sort(reverse=True)


def optmize_me(x, y):
    # for x = y == (1, 1) and (-1, -1)
    # for y = -x == (1, 1) and (-1, -1)
    return (x - y) * (1 - x * y)


def random_gene():
    gene = Gene()
    gene.shuffle_genomes()

    return gene


if __name__ == '__main__':
    main()
