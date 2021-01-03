#!/bin/sh

# for unit testing with pytest
# specify all the unit test files

tests=(\
	examples/a.py\
	examples/b.py\
);
for t in ${tests[@]}; do
	pytest $t;
	[ "$?" -eq 1 ] && exit 1;
done
exit 0;
