from .behavior import poison, doctor, build
from .mechanism import resolve_Poison_Tree, is_Tree_Sick, is_Tree_Dead, resolve_Build_Patio, resolve_Tree_Doctor, resolve_Alice, resolve_Bob

psubs = [
    { 
        'label': 'Does Alice Poison the  Tree?',
        'policies': {
            'poison tree': poison,
        },
        'variables': {
            'Alice': resolve_Poison_Tree,
            'World': is_Tree_Sick
        }
    },
        { 
        'label': 'Does Bob Call the Tree Doctor? And Does Alice Build a Patio',
        'policies': {
            'tree doctor': doctor,
            'build patio': build
        },
        'variables': {
            'Alice': resolve_Build_Patio,
            'Bob': resolve_Tree_Doctor,
            'World': is_Tree_Dead
        }
    },
        { 
        'label': 'Compute Utility Variables and Update Strategies',
        'policies': {
        },
        'variables': {
            'Alice': resolve_Alice,
            'Bob': resolve_Bob,
        }
    }
]