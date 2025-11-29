class PlannerAgent:
    def __init__(self):
        pass

    def decompose(self, command):
        # simplistic mapping: only supports "Analyze ROAS drop" style commands
        tasks = ['load_data','summarize','generate_hypotheses','validate','generate_creatives','save_outputs']
        return {'command': command, 'tasks': tasks}