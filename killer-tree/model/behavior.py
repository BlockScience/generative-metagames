import numpy as np

class Alice:

    def __init__(self):
       
       self.strategy = { }

    def poison_decision(self, observables):
        """
        Method Alice uses to decide whether to poison the tree
        """

        print(observables)
        # should be augmented to depend on strategy
        decision = bool(np.random.randint(0,2))

        return decision

    def build_decision(self, observables):
        """
        Method Alice uses to decide whether to build her patio
        """

        print(observables)
        # should be augmented to depend on strategy
        decision = bool(np.random.randint(0,2))

        return decision
    
    def update_strategy(self, observables):
        """
        Method Alice uses to update her strategy based on outcomes
        """
        print(observables)
        self.strategy = {}

        
class Bob:

    def __init__(self):

        self.strategy = { }

    def doctor_decision(self, observables):
        """
        Method Bob Uses to decide whether to call the Tree Doctor
        """

        print(observables)
        # should be augmented to depend on strategy
        decision = bool(np.random.randint(0,2))

        return decision

    def update_strategy(self, observables):
        """
        Method Bob uses to update her strategy based on outcomes
        """

        print(observables)
        self.strategy = {}

### methods below provide wrappers to ensure modularity

def poison(params, step, prev_state, state):
    """
    psub wrapper method for Alice's Poison Tree decison
    """
    alice = state['Alice']['Agent']
    observables = {}
    decision = alice.poison_decision(observables)
    
    return {"poison": decision}

def build(params, step, prev_state, state):
    """
    psub wrapper method for Alice's Build Patio decison
    """
    alice = state['Alice']['Agent']
    observables = {'poison':state['Alice']['Poison Tree Decision'],'sick':state['World']['Tree Sick Outcome']}
    decision = alice.build_decision(observables)
    
    return {"build": decision}

def doctor(params, step, prev_state, state):
    """
    psub wrapper method for Bob's Tree Doctor decision
    """
    bob = state['Bob']['Agent']
    observables = {'sick':state['World']['Tree Sick Outcome']}
    decision = bob.doctor_decision(observables)
    
    return {"doctor": decision}