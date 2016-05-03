import random


class Node(object):

    def __init__(self, ip, port, tox_key, rand):
        self._ip, self._port, self._tox_key, self.rand = ip, port, tox_key, rand

    def get_data(self):
        return self._ip, self._port, self._tox_key


def node_generator():
    nodes = []
    ips = [
        "144.76.60.215", "23.226.230.47", "195.154.119.113", "biribiri.org",
        "46.38.239.179", "178.62.250.138", "130.133.110.14", "104.167.101.29",
        "205.185.116.116", "198.98.51.198", "80.232.246.79", "108.61.165.198",
        "212.71.252.109", "194.249.212.109", "185.25.116.107", "192.99.168.140",
        "46.101.197.175", "95.215.46.114", "5.189.176.217", "148.251.23.146",
        "104.223.122.15", "78.47.114.252", "d4rk4.ru", "81.4.110.149",
        "95.31.20.151", "104.233.104.126", "51.254.84.212", "home.vikingmakt.com.br",
        "5.135.59.163", "185.58.206.164", "188.244.38.183", "mrflibble.c4.ee",
        "82.211.31.116", "128.199.199.197", "103.230.156.174", "91.121.66.124",
        "92.54.84.70", "tox1.privacydragon.me"
    ]
    ports = [
        33445, 33445, 33445, 33445,
        33445, 33445, 33445, 33445,
        33445, 33445, 33445, 33445,
        33445, 33445, 33445, 33445,
        443, 33445, 5190, 2306,
        33445, 33445, 1813, 33445,
        33445, 33445, 33445, 33445,
        33445, 33445, 33445, 33445,
        33445, 33445, 33445, 33445,
        33445, 33445
    ]
    ids = [
        "04119E835DF3E78BACF0F84235B300546AF8B936F035185E2A8E9E0A67C8924F",
        "A09162D68618E742FFBCA1C2C70385E6679604B2D80EA6E84AD0996A1AC8A074",
        "E398A69646B8CEACA9F0B84F553726C1C49270558C57DF5F3C368F05A7D71354",
        "F404ABAA1C99A9D37D61AB54898F56793E1DEF8BD46B1038B9D822E8460FAB67",
        "F5A1A38EFB6BD3C2C8AF8B10D85F0F89E931704D349F1D0720C3C4059AF2440A",
        "788236D34978D1D5BD822F0A5BEBD2C53C64CC31CD3149350EE27D4D9A2F9B6B",
        "461FA3776EF0FA655F1A05477DF1B3B614F7D6B124F7DB1DD4FE3C08B03B640F",
        "5918AC3C06955962A75AD7DF4F80A5D7C34F7DB9E1498D2E0495DE35B3FE8A57",
        "A179B09749AC826FF01F37A9613F6B57118AE014D4196A0E1105A98F93A54702",
        "1D5A5F2F5D6233058BF0259B09622FB40B482E4FA0931EB8FD3AB8E7BF7DAF6F",
        "CF6CECA0A14A31717CC8501DA51BE27742B70746956E6676FF423A529F91ED5D",
        "8E7D0B859922EF569298B4D261A8CCB5FEA14FB91ED412A7603A585A25698832",
        "C4CEB8C7AC607C6B374E2E782B3C00EA3A63B80D4910B8649CCACDD19F260819",
        "3CEE1F054081E7A011234883BC4FC39F661A55B73637A5AC293DDF1251D9432B",
        "DA4E4ED4B697F2E9B000EEFE3A34B554ACD3F45F5C96EAEA2516DD7FF9AF7B43",
        "6A4D0607A296838434A6A7DDF99F50EF9D60A2C510BBF31FE538A25CB6B4652F",
        "CD133B521159541FB1D326DE9850F5E56A6C724B5B8E5EB5CD8D950408E95707",
        "5823FB947FF24CF83DDFAC3F3BAA18F96EA2018B16CC08429CB97FA502F40C23",
        "2B2137E094F743AC8BD44652C55F41DFACC502F125E99E4FE24D40537489E32F",
        "7AED21F94D82B05774F697B209628CD5A9AD17E0C073D9329076A4C28ED28147",
        "0FB96EEBFB1650DDB52E70CF773DDFCABE25A95CC3BB50FC251082E4B63EF82A",
        "1C5293AEF2114717547B39DA8EA6F1E331E5E358B35F9B6B5F19317911C5F976",
        "53737F6D47FA6BD2808F378E339AF45BF86F39B64E79D6D491C53A1D522E7039",
        "9E7BD4793FFECA7F32238FA2361040C09025ED3333744483CA6F3039BFF0211E",
        "9CA69BB74DE7C056D1CC6B16AB8A0A38725C0349D187D8996766958584D39340",
        "EDEE8F2E839A57820DE3DA4156D88350E53D4161447068A3457EE8F59F362414",
        "AEC204B9A4501412D5F0BB67D9C81B5DB3EE6ADA64122D32A3E9B093D544327D",
        "188E072676404ED833A4E947DC1D223DF8EFEBE5F5258573A236573688FB9761",
        "2D320F971EF2CA18004416C2AAE7BA52BF7949DB34EA8E2E21AF67BD367BE211",
        "24156472041E5F220D1FA11D9DF32F7AD697D59845701CDD7BE7D1785EB9DB39",
        "15A0F9684E2423F9F46CFA5A50B562AE42525580D840CC50E518192BF333EE38",
        "FAAB17014F42F7F20949F61E55F66A73C230876812A9737F5F6D2DCE4D9E4207",
        "AF97B76392A6474AF2FD269220FDCF4127D86A42EF3A242DF53A40A268A2CD7C",
        "B05C8869DBB4EDDD308F43C1A974A20A725A36EACCA123862FDE9945BF9D3E09",
        "5C4C7A60183D668E5BD8B3780D1288203E2F1BAE4EEF03278019E21F86174C1D",
        "4E3F7D37295664BBD0741B6DBCB6431D6CD77FC4105338C2FC31567BF5C8224A",
        "5625A62618CB4FCA70E147A71B29695F38CC65FF0CBD68AD46254585BE564802",
        "31910C0497D347FF160D6F3A6C0E317BAFA71E8E03BC4CBB2A185C9D4FB8B31E"
    ]
    for i in xrange(len(ips)):
        nodes.append(Node(ips[i], ports[i], ids[i], random.randint(0, 1000000)))
    arr = sorted(nodes, key=lambda x: x.rand)[:4]
    for elem in arr:
        yield elem.get_data()
