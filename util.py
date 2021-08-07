def translate_to_branch(id, description):
    return "feature/{}-{}".format(
        id,
        description.replace(" - ", "-")
        .replace(".", "_")
        .replace(",", "_")
        .replace("/", "")
        .replace("[", "(")
        .replace("]", ")")
        .replace(": ", "-")
        .replace(" ", "-")
        .replace("'", "")
        .rstrip("_")
    )
