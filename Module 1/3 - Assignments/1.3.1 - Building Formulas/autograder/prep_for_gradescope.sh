#!/bin/bash
#rm data/extras/*.txt
#rm data/extras/*.csv

#rm data/*.txt
#rm data/*.csv

zip -r autograder.zip * -x "data/*.csv" -x "data/*.txt" -x "*.DS_Store" -x "*student_submission.py"