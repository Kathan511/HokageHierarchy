"""
This is main handler script for interacting with API services.
"""

from _setup import __version__
from _setup import __loggroup_name__
import traceback
from iqmloggerutils import IQMLogger
from iqmpyutils.common import get_config as get_config_object
from apis.ecs import run_ecs_task

logger = IQMLogger(log_group_name=__loggroup_name__, log_stream_name=__module_name__, project_name=__loggroup_name__,
                   version=__version__)


def function_name(YOUR_PARAMS):
    '''
    General function to trigger to run ECS task
    '''
    cfg = get_config_object('config/config_name.config', mode)

    config_path = cfg['PATH_OF_CORE_CONFIG']

    try:
        logger.log('Add data trigerred for {}'.format(module))
        # provisioning ecs task
        logger.log("Launching ETL Task for {}".format(module))
        run_ecs_task(YOUR_PARAMS)
        logger.log("Task created successfully.")
        message = 'YOUR_MESSAGE'
        logger.log(message)
        
        return {'statusCode': 200,
                'responseObject': {'message': message}}

    except Exception as e:
        error = traceback.format_exc()
        logger.err("{'state':'%s', 'message':'%s'}" % ('All', error), uid='ErrorRunTask')
        return {'statusCode': 500, 'responseObject':
            {'message': "YOUR_MESSAGE"}
