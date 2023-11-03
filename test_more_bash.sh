echo 'entering in'
TEST='Rishabh is learning'  ## no spaces between = else error in bash

a=10

if [ $a -lt $1 ]
then
    echo 'maza aa gya'
else
    echo 'nhi aya bro'
fi

for (( k=0;k<10;k++ )); do  ## double brackets around arithmetic instructions
    a=$((2*k+2))
    echo $a
done

if [[ $a -lt $2 ]] ## may be single or double doesn matter
then
    echo 'maza aa gya'
else
    echo 'nhi aya bro'
fi

## ./run.sh sources and runs the code
## --foo long form options vs -al which usually works as -a then -l