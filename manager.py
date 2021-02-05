import dog
import datetime

atlas = dog.Dog("Atlas", 3, "M")
print(atlas.name)


dag = dog.Dog("Dagny", 2, "F", datetime.datetime(2021, 2, 5))
print(dag.last_heat.year)
