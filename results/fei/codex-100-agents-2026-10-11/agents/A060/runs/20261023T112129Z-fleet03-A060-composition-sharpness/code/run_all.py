import pair
pair.graph_run('main')
pair.CHECKS=0
pair.mixed()
pair.CHECKS=0
pair.failures()
pair.CHECKS=0
pair.graph_run('reproduce')
