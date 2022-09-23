#! bin.bash
# Get all maps with json extension from maps directory and save them to txt file
find ./maps -type f -name "*.json" > output.txt

# Iterate through each map and run tha game with our code
filename='output.txt'
n=1
while read line; do
python main.py --players 7 --seed 1234 --skill 100 --map $line
n=$((n+1))
done < $filename
