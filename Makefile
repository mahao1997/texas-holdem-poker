test:
	mkdir -p test-results
	python3 -m pytest \
	    --cov=./ \
	    --no-cov-on-fail \
	    --cov-report=html:test-results/htmlcov \
	    --cov-report term \
	    --doctest-modules \
	    --junitxml=test-results/junit.xml \
	    ./
	python3 -m coverage xml -o test-results/coverage.xml