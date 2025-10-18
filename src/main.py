from Algoritma import HC_SA, SimulatedAnnealing, GeneticAlgorithm
import sys, os
import json, time

if __name__ == "__main__":
    if len(sys.argv) < 3:
        os.makedirs("output", exist_ok=True)
        print("Usage:")
        print("Algorithm options: hc (Hill Climbing Steepest Ascent), sa (Simulated Annealing), ga (Genetic Algorithm)\n")
        print("1. python main.py <algorithm> <input.json> <population_size>* <generations num>*")
        print("e.g: python main.py ga input/input_1.json 10 10  OR  python main.py hc input/input_1.json\n")
        print("2. python main.py experiment <input.json>")
        print("e.g: python main.py experiment input/input_1.json\n")
        print("NOTE: * indicates optional arguments for Genetic Algorithm only.")
        sys.exit(1)

    algorithm = sys.argv[1]
    input_source = sys.argv[2]

    with open(sys.argv[2], "r") as f:
        input_file = json.load(f)

    match algorithm:
        case "hc":
            hill_climbing = HC_SA(input=input_file)
            hill_climbing.run(verbose=True, name="HC_main_")
        case "sa":
            simulated_annealing = SimulatedAnnealing(input=input_file)
            simulated_annealing.run(verbose=True, name="SA_main_")
        case "ga":
            if sys.argv[3] and sys.argv[4]:
                population_size = int(sys.argv[3])
                generasi = int(sys.argv[4])
            else:
                print("For Genetic Algorithm, please provide population size and number of generations.")
                sys.exit(1)
        
            genetic_algorithm = GeneticAlgorithm(input=input_file, population_size=population_size, n_generasi=generasi)
            genetic_algorithm.run(verbose=True, name="GA_main")

        case "experiment":
            # HC_SA
            print("Eksperimen HC")
            print("\nEksperimen variasi 1")
            start_time = time.time()
            hill_climbing_1 = HC_SA(input=input_file, seed=1)
            hill_climbing_1.run(name="HC_variasi1")
            end_time = time.time()
            hill_climbing_1.fungsi_objektif(verbose=True)
            print(hill_climbing_1.iteration, "iterations")
            hill_climbing_1.plot("HC1_plot")
            print(f"Durasi variasi HC 1: {end_time - start_time}s")

            print("\nEksperimen variasi 2")
            start_time = time.time()
            hill_climbing_2 = HC_SA(input=input_file, seed=2)
            hill_climbing_2.run(name="HC_variasi2")
            end_time = time.time()
            hill_climbing_2.fungsi_objektif(verbose=True)
            print(hill_climbing_2.iteration, "iterations")
            hill_climbing_2.plot("HC2_plot")
            print(f"Durasi variasi HC 2: {end_time - start_time}s")

            print("\nEksperimen variasi 3")
            start_time = time.time()
            hill_climbing_3 = HC_SA(input=input_file, seed=3)
            hill_climbing_3.run(name="HC_variasi3")
            end_time = time.time()
            hill_climbing_3.fungsi_objektif(verbose=True)
            print(hill_climbing_3.iteration, "iterations")
            hill_climbing_3.plot("HC3_plot")
            print(f"Durasi variasi HC 3: {end_time - start_time}s")


            # Simulated Annealing
            print("\nEksperimen Simulated Annealing")
            print("\nEksperimen variasi 1")
            start_time = time.time()
            simulated_annealing_1 = SimulatedAnnealing(input=input_file, seed=1)
            simulated_annealing_1.run(name="SA_variasi1")
            end_time = time.time()
            simulated_annealing_1.plot(name="SA1_plot")
            simulated_annealing_1.fungsi_objektif(verbose=True)
            print('Frekuensi stuck di local optima:', simulated_annealing_1.stuck_count)
            print(f"Durasi variasi Simulated Annealing 1: {end_time - start_time}s")

            print("\nEksperimen variasi 2")
            start_time = time.time()
            simulated_annealing_2 = SimulatedAnnealing(input=input_file, seed=2)
            simulated_annealing_2.run(name="SA_variasi2")
            end_time = time.time()
            simulated_annealing_2.fungsi_objektif(verbose=True)
            simulated_annealing_2.plot(name="SA2_plot")
            print('Frekuensi stuck di local optima:', simulated_annealing_2.stuck_count)
            print(f"Durasi variasi Simulated Annealing 2: {end_time - start_time}s")

            print("\nEksperimen variasi 3")
            start_time = time.time()
            simulated_annealing_3 = SimulatedAnnealing(input=input_file, seed=3)
            simulated_annealing_3.run(name="SA_variasi3")
            end_time = time.time()
            simulated_annealing_3.fungsi_objektif(verbose=True)
            simulated_annealing_3.plot(name="SA3_plot")
            print('Frekuensi stuck di local optima:', simulated_annealing_3.stuck_count)
            print(f"Durasi variasi Simulated Annealing 3: {end_time - start_time}s")


            # Genetic Algorithm
            print("\nEksperimen Genetic Algorithm")
            print("\nEksperimen variasi 1, n_generasi: 200, populasi: 30")
            start_time = time.time()
            genetic_1 = GeneticAlgorithm(input=input_file, population_size=30, n_generasi=200)
            genetic_1.run(name="GA_variasi1")
            end_time = time.time()
            genetic_1.plot(name="GA1_plot")
            print(f"Durasi variasi Genetic Algorithm 1: {end_time - start_time}s")

            print("\nEksperimen variasi 2, n_generasi: 200, populasi: 70")
            start_time = time.time()
            genetic_2 = GeneticAlgorithm(input=input_file, population_size=70, n_generasi=200)
            genetic_2.run(name="GA_variasi2")
            end_time = time.time()
            genetic_1.plot(name="GA2_plot")
            print(f"Durasi variasi Genetic Algorithm 2: {end_time - start_time}s")

            print("\nEksperimen variasi 3, n_generasi: 200, populasi: 120")
            start_time = time.time()
            genetic_3 = GeneticAlgorithm(input=input_file, population_size=120, n_generasi=200)
            genetic_3.run(name="GA_variasi3")
            end_time = time.time()
            genetic_1.plot(name="GA3_plot")
            print(f"Durasi variasi Genetic Algorithm 3: {end_time - start_time}s")

            print("\nEksperimen variasi 4, n_generasi: 100, populasi: 200")
            start_time = time.time()
            genetic_1 = GeneticAlgorithm(input=input_file, n_generasi=100, population_size=200)
            genetic_1.run(name="GA_variasi4")
            end_time = time.time()
            genetic_1.plot(name="GA4_plot")
            print(f"Durasi variasi Genetic Algorithm 1: {end_time - start_time}s")

            print("\nEksperimen variasi 5, n_generasi: 200, populasi: 200")
            start_time = time.time()
            genetic_2 = GeneticAlgorithm(input=input_file, n_generasi=200, population_size=200)
            genetic_2.run(name="GA_variasi5")
            end_time = time.time()
            genetic_1.plot(name="GA5_plot")
            print(f"Durasi variasi Genetic Algorithm 2: {end_time - start_time}s")

            print("\nEksperimen variasi 6, n_generasi: 500, populasi: 200")
            start_time = time.time()
            genetic_3 = GeneticAlgorithm(input=input_file, n_generasi=500, population_size=200)
            genetic_3.run(name="GA_variasi6")
            end_time = time.time()
            genetic_1.plot(name="GA6_plot") 
            print(f"Durasi variasi Genetic Algorithm 3: {end_time - start_time}s")