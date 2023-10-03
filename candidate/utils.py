"""Modula that has some helper functions."""


def resume_upload_path(instance, filename: str) -> str:
    """Create a unique path for media based on the instance and filename.

    This function will a unique timestamp using the created time
    to create a unique path

    Args:
        instance (Candidate): Instance from Candidate that have been created.
        filename (str): The name of the file that have been uploaded.

    Returns:
        str: a unique path for uploading the file.
    """
    # Get the full_name of the candidate and sanitize it (e.g., remove spaces)
    full_name: str = instance.full_name.replace(" ", "_")
    # We will use the created date so the candidates with same name
    # We cannot use the id because it is None at this point
    created_date_str: str = instance.created_at.strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]
    # Build the dynamic upload path using the candidate's full_name
    return "candidates/{0}-{1}/{2}".format(full_name, created_date_str, filename)
