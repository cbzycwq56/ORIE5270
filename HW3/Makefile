cover:
	make cover_tests


cover_tests:
	py.test -s  --cov-config .coveragerc --cov Graph \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	Test
