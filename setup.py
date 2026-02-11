from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_vuillermet2012grammar',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_vuillermet2012grammar'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'vuillermet2012grammar=cldfbench_vuillermet2012grammar:Dataset',
        ]
    },
    install_requires=[
        'pyglottography>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
