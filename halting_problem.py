def halting_oracle(f, input):
    # Pretpostavimo da ova funkcija može riješiti problem zaustavljanja.
    result = f(input)
    if result == "halt":
        return True
    else:
        return False

def paradoxical_program(halt_oracle):
    # Definira paradoks
    def g(input):
        if halt_oracle(g, input):
            #  Ako se g zaustavi na ulazu, ući će u beskonačnu petlju.
            while True:
                pass
        else:
            # Ako se g ne zaustavi na ulazu, zaustavit će se.
            return "halt"
    return g

def main():
    halt_oracle = halting_oracle
    paradox = paradoxical_program(halt_oracle)
    result = halt_oracle(paradox, paradox)
    # Ovo dovodi do kontradikcije jer rezultat mora biti ili True ili False.
    # Rezultat True dovodi do beskonačne petlje.
    # Rezultat false dovodi do zaustavljanja.
    # Pretpostavka da halting_oracle može riješiti problem zaustavljanja je netočna.

if __name__ == "__main__":
    main()