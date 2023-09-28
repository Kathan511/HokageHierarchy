"""
This module defines ecs fargate functions.
"""
import boto3
import traceback
from iqmpyutils.common import get_config

def run_ecs_task(YOUR_PARAMS):
    """
    """
    cfg = get_config('apis/ecs.config', mode)

    try:
        """
        Your parameters list that you want to send to the ECS
        command_list = ['-c',config,'-m', mode,'-of',output_format, '-ut', str(upload_type),
                        '-fid', str(file_id), '-sip', str(int(save_intermediate_polygons)),'-res', str(resolution)]
        """

        client = boto3.client('ecs')
        security_groups=cfg['security_group'].split(',')
        security_groups.append(cfg['security_group_ecs_exporter'])
        response = client.run_task(
            cluster=cfg['cluster'],
            launchType=cfg['task_type'],
            taskDefinition=cfg['task_family_name'],
            count=1,
            platformVersion='LATEST',
            propagateTags='TASK_DEFINITION',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [
                        cfg['subnet1'],
                        cfg['subnet2']
                    ],
                    'securityGroups': security_groups,
                    'assignPublicIp': 'DISABLED'
                }
            },
            overrides={
                'containerOverrides': [{
                    'name': cfg['task_family_name'],
                    'command': command_list
                }]
            })
    except Exception as e:
        error = traceback.format_exc()
        logger.err("{'state':'%s', 'message':'%s'}" % ('All', error), uid='ErrorRunTask')
        raise e
