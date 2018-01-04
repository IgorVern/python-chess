import platform


class Colors:
    white = 'WHITE'
    black = 'BLACK'


linux_white = dict(king=u'\u265a',
                   queen=u'\u265b',
                   rook=u'\u265c',
                   bishop=u'\u265d',
                   knight=u'\u265e',
                   pawn=u'\u265f')

linux_black = dict(king=u'\u2654',
                   queen=u'\u2655',
                   rook=u'\u2656',
                   bishop=u'\u2657',
                   knight=u'\u2658',
                   pawn=u'\u2659')

windows_white = dict(king='K',
                     queen='Q',
                     rook='R',
                     bishop='B',
                     knight='N',
                     pawn='P')

windows_black = dict(king='k',
                     queen='q',
                     rook='r',
                     bishop='b',
                     knight='n',
                     pawn='p')


class PiecesSymbols:
    black = windows_black if platform.system() == 'Windows' else linux_black

    white = windows_white if platform.system() == 'Windows' else linux_white
