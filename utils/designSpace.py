#!/usr/bin/env python
# encoding: utf-8
# @author: jiangqi
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: jiangqi@zjut.edu.com
# @file: designSpace.py
# @time: 2022/1/10 12:52
designSpace = {
    'Q': {
        'combination': 'Q',
        'support': True,
        'tasks': ['distribution'],
        'visualizations': ['histogram', 'stripplot', 'boxplot'],
        'designs': [
            {
                'task': 'distribution',
                'vis_type': 'stripplot',
                'not_suggested_by_default': False,
                'mark': 'tick',
                'mandatory': ['x'],
                'priority': ['x'],
                'x': {'is_defined': False, 'agg': None}
            },
            {
                'task': 'distribution',
                'vis_type': 'boxplot',
                'not_suggested_by_default': False,
                'mark': 'boxplot',
                'mandatory': ['x'],
                'priority': ['x'],
                'x': {'is_defined': False, 'agg': None}
            }]
    },
    'N': {
        'combination': 'N',
        'support': True,
        'tasks': ['distribution'],
        'visualizations': ['barchart', 'piechart', 'boxplot', 'stripplot'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'agg_type': 'count'
        },
            {
                'task': 'proportion',
                'vis_type': 'piechart',
                'not_suggested_by_default': False,
                'mark': 'arc',
                'mandatory': ['theta', 'color'],
                'priority': ['theta', 'color'],
                'theta': {'attr': None, 'is_defined': False, 'agg': None},
                'color': {'attr': None, 'is_defined': False, 'attr_ref': 'theta', 'agg': 'count'},
                'agg_type': 'count'
            },
        ]
    },
    'T': {
        'combination': 'T',
        'support': True,
        'tasks': ['trend'],
        'visualizations': ['linechart', 'areachart'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }]
    },
    'QQ': {
        'combination': 'QQ',
        'support': True,
        'tasks': ['correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QN': {
        'combination': 'QN',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['barchart', 'boxplot'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'proportion',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }
        ]
    },
    'QT': {
        'combination': 'QT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }]
    },
    'NN': {
        'combination': 'NN',
        'support': True,
        'tasks': ['distribution'],
        'visualizations': ['scatterplot', 'barchart'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'NO': {
        'combination': 'NO',
        'support': True,
        'tasks': ['distribution'],
        'visualizations': ['scatterplot', 'barchart'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'NT': {
        'combination': 'NT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }]
    },
    'TT': {
        'combination': 'TT',
        'support': False,
        'tasks': [],
        'visualizations': [],
        'designs': []
    },
    'QQQ': {
        'combination': 'QQQ',
        'support': True,
        'tasks': ['correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QQN': {
        'combination': 'QQN',
        'support': True,
        'tasks': ['correlation', 'distribution'],
        'visualizations': ['scatterplot', 'stripplot'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QQO': {
        'combination': 'QQO',
        'support': True,
        'tasks': ['correlation', 'distribution'],
        'visualizations': ['scatterplot', 'stripplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QQT': {
        'combination': 'QQT',
        'support': True,
        'tasks': ['correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNN': {
        'combination': 'QNN',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNO': {
        'combination': 'QNO',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNT': {
        'combination': 'QNT',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'barchart', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }]
    },
    'QOO': {
        'combination': 'QOO',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QOT': {
        'combination': 'QOT',
        'support': True,
        'tasks': ['derived_value', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'barchart', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }]
    },
    'NNT': {
        'combination': 'NNT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }]
    },
    'NOT': {
        'combination': 'NOT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }]
    },
    'OOT': {
        'combination': 'OOT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'areachart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'areachart',
            'not_suggested_by_default': True,
            'mark': 'area',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }]
    },
}
