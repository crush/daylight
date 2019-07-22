from typing import List, Union

import daylight.db.models as models


# Returned by the `DaylightDB` when a query is executed to retrieve data or a
# mutation has been applied to mutate it.
State = Union[
    models.User,
    List[models.User],
    models.Match,
    List[models.Match],
    models.Like,
    List[models.Like],
    models.Profile,
    List[models.Profile],
    models.Tag,
    List[models.Tag],
    models.Photo,
    List[models.Photo],
    models.WomanFemmeAccountType,
    List[models.WomanFemmeAccountType],
    models.ManMascAccountType,
    List[models.ManMascAccountType]
]

