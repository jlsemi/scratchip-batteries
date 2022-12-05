install-local:
	if [ -d "dist" ]; then rm -r dist; fi
	if [ -d "build" ]; then rm -r build; fi
	python3 setup.py bdist_wheel
	python3 -m pip uninstall scratchip-batteries -y
	python3 -m pip install --user `ls dist/*.whl`
