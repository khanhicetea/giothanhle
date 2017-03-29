import re


def noAccentVietnamese(text):
    text = text.lower()
    text = re.sub('à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ', 'a', text)
    text = re.sub('è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ', 'e', text)
    text = re.sub('ì|í|ị|ỉ|ĩ', 'i', text)
    text = re.sub('ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ', 'o', text)
    text = re.sub('ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ', 'u', text)
    text = re.sub('ỳ|ý|ỵ|ỷ|ỹ', 'y', text)
    text = re.sub('đ', 'd', text)
    text = re.sub('!|@|%|\^|\*|\(|\)|\+|\=|\<|\>|\?|\/|,|\.|\:|\;|\'|\"|\&|\#|\[|\]|~|$|_', '', text)
    return text