from Lesson_9_PageObject_OOP_Final import demoqa_tests


def resource(relative_path):

    from pathlib import Path
    return (
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
