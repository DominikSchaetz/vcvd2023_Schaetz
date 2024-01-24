#required imports
import argparse
import s2310710033 as calculation


#setup arg parser

parser = argparse.ArgumentParser()
parser.add_argument('mass', type=float, help="Vehicle mass")
parser.add_argument('velocity', type=float, help="Vehicle velocity")
parser.add_argument('friction', type=float, help="Friction")

args = parser.parse_args()

#method

def main():
     calculation.deceleration(args)

#call methode

if __name__ == "__main__":
    main()

