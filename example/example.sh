python ../simucache/Main.py -h
python ../simucache/Main.py -t 10 -hi 1 -s -n 4 -c LFU -f ZIPF -cs 2 -z 1; # without e and with ZIPF distribution. Need -z > 0
python ../simucache/Main.py -t 10 -hi 1 -s -n 4 -c FIFO -f UNIFORM -cs 2 -e 0.03 -i 0 1 -d 2 3; # specifying increase and decrease files
python ../simucache/Main.py -t 10 -hi 1 -s -n 5 -c RAND -f RANDOM -cs 2 -e 0.03 0.02 -0.02 -0.01 -0.02; # with variable e to each file
python ../simucache/Main.py -t 10 -hi 1 -s -n 5 -c LRU -f PERSONAL -cs 2 -l 0.2 0.3 0.1 0.2 0.2; # with different access frequencies to each file
