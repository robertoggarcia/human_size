
def human_size(bytes):
    if bytes >= 1 * (10**24):
        return "%.1f%s" % (bytes/(1 * (10**24)), 'YB')
    units = ['bytes', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    for unit in units:
        if bytes < 1000:
            return "%.1f%s" % (bytes, unit)
        bytes /= 1000
