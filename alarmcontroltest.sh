ALARM_TIME=$1
echo ALARM_TIME

python alarmtextgen.py $ALARM_TIME > tempalarmtext

cat tempalarmtext | while read line; do
	echo $line
	./speech.sh $line
done
pianobar
