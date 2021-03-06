#   Copyright 2020 Ashish Kurmi
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License

from lib import account_iterator
from lib import s3
from lib import utility


def create(event):
    """ Create inventory configurations

    Arguments:
        event {json} -- Lambda execution event

    Returns:
        json -- Lambda input for the next Step Function task
    """
    return account_iterator.iterate(event, s3.create_inventory_configuration_helper)


@utility.setup_logger
def lambda_handler(event, context):
    """ Lambda handler

    Arguments:
        event {[type]} -- AWS Lambda event object
        context {[type]} -- AWS Lambda context object

    Returns:
        json -- Lambda input for the next Step Function task
    """
    return create(event)
