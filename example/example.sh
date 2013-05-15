#python ../simucache/Main.py -h
python ../simucache/Main.py -t 10 -hi 1 -s -n 4 -c FIFO -f UNIFORM -cs 2 -e 0.03 -i 0 1 -d 2 3;
python ../simucache/Main.py -t 10 -hi 1 -s -n 5 -c RAND -f RANDOM -cs 2 -e 0.03 0.02 -0.02 -0.01 -0.02;
python ../simucache/Main.py -t 10 -hi 1 -s -n 5 -c LRU -f PERSONAL -cs 2 -l 0.2 0.2 0.2 0.2 0.2;
