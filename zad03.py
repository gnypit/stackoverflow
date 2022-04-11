import pyswarms
from pyswarms.utils.functions import single_obj
from pyswarms.backend.topology import Ring
from pyswarms.utils.plotters.plotters import plot_surface
from pyswarms.utils.plotters.formatters import Mesher
from pyswarms.utils.plotters.formatters import Designer


options = {'c1': 0.4, 'c2': 0.5, 'w': 0.9, 'p': 2, 'k': 2}
optimizer_ring = pyswarms.single.GeneralOptimizerPSO(
    n_particles=10, dimensions=2, options=options, topology=Ring(static=False)
)

stats = optimizer_ring.optimize(single_obj.levi, iters=100)
m = Mesher(single_obj.levi)

pos_history_3d = m.compute_history_3d(optimizer_ring.pos_history)
d = Designer(limits=[(-10, 10), (-10, 10), (0, 100)], label=['x-axis', 'y-axis', 'z-axis'])

animation3d = plot_surface(
    pos_history=pos_history_3d, mesher=m, designer=d, mark=(1, 1, 0))

animation3d.save('plot2.gif', writer='imagemagick', fps=10)
