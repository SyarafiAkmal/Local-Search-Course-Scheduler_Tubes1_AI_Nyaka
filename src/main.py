from Algoritma import HC_SA, SimulatedAnnealing, GeneticAlgorithm
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("1. python Main.py <algorithm> <input.json> <population_size>* <generations num>* ")
        print("2. python Main.py experiment <input.json>")
        print("Note: * indicates optional arguments for Genetic Algorithm only.")
        print("Algorithm options: hc (Hill Climbing Steepest Ascent), sa (Simulated Annealing), ga (Genetic Algorithm)")
        sys.exit(1)

    algorithm = sys.argv[1]
    input_source = sys.argv[2]

    with open(sys.argv[2], "r") as f:
        input_file = json.load(f)

    match algorithm:
        case "hc":
            hill_climbing = HC_SA(input=input_file)
            hill_climbing.run()
        case "sa":
            simulated_annealing = SimulatedAnnealing(input=input_file)
            simulated_annealing.run(verbose=True)
        case "ga":
            if sys.argv[3] and sys.argv[4]:
                population_size = int(sys.argv[3])
                n_generasi = int(sys.argv[4])
            else:
                print("For Genetic Algorithm, please provide population size and number of generations.")
                sys.exit(1)
        
            genetic_algorithm = GeneticAlgorithm(input=input_file, population_size=population_size)
            genetic_algorithm.run(verbose=True, n_generasi=n_generasi)