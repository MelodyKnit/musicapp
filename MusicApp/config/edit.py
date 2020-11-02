from json import dump, loads
from os import makedirs
from os.path import dirname
from re import sub
base64_icon = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAASwklEQVR4Xu2dC5BdRZnH/9/cTGYmMQ+RBDLRJIBJ8EFCqaiEkofy2CBq7YIilKKrrLWbKlCjUAplqSVLuW4USLSyJWWo5SkiAiGQEF4BJOBWBDIEJAmQzEyGTFgySUgm87r39lbfOdkM45073eecPn3uPf+uunVT0P1196/7N30efc4VMJEACYxIQMiGBEhgZAIUhLODBCoQoCCcHiRAQTgHSCAcAa4g4bixVEYIUJCMDDS7GY4ABQnHjaUyQoCCZGSg2c1wBChIOG4slRECFCQjA81uhiNAQcJxY6mMEKhKQZRSYwHMDD4zhvxb/zcm/wS2A2gFoL9LHxHR31WXqkIQpdSpAM4FcFogw7SqI80GawKHhLkPwIMisiXtWFIpiFJqSiDEWQDOBHBU2kGyfaEItABYCeBxAOtEpBgqisNCqRJEKXUpgC8EUjQ67DdDp49AO4DHAPxeRNakpXmpEEQp9XkAlwP4TFrAsB1eCdwM4AYRec5rKwB4FUQp9QkA3wZwkW8QrD91BPoBLA1E2eGrdV4EUUodE4ih5WAigUoEtBw3aFlEREuTaEpcEKXU1wD8AsDURHvKyqqdgD7c+qGIrE2yI4kKopS6EsB/JNlB1lVzBK4QkSVJ9SoxQZRSvwSwOKmOsZ6aJnCLiFySRA+dC6KUGqevcQM4KYkOsY7MEGgRkfmue+tUEKXU8QD+5roTjJ9pAvNFRN9wdJKcCaKU+iCAl5y0mkFJ4J0EjhKRN11AcSKIUkrfBe8GUOei0YxJAsMIdInIe1xQcSWIPqzSh1dMJJAUgdtE5CtxVxa7IEopvVNTbx1hIoGkCXxXRK6Ps9JYBVFK/SeA78fZQMYiAUsC54vInyzLjJg9NkGUUv8C4LdxNYxxSCAkgS4A54jIhpDl31EsFkGCvVXPcvtIHEPCGDEQWCMiC2OIE89uXqWUPu7jxsM4RoQx4iLwNRHR2+YjpcgrSLBlXa8eTCSQJgJ6c+PJUXcAxyHI7XyeI03zgm0ZQiDyxsZIggRPAurLukwkkEYC+lkSvYqEfuAqqiCP8DHZNM4LtmkIgSUickVYIqEFCV6wcGPYilmOBBIioJ9C1KtIqOfbowhyb/AGkoT6yWpIIDSBH4nINWFKhxJEKXUEAH1c1xSmUpYhgYQJPCEip4epM6wg5wP4Y5gKWYYEPBGYJSL6dahWKawgvwGwyKomZiYBvwQWichy2yaEFaQDQLNtZcxPAh4JrBQR/dZOq2QtiFLq4wD+YlULM5OAfwIHRWS8bTPCCKKvBlxtWxHzk0AKCCy0fe9vGEGeBrAgBZ1lE0jAlsC1ImL1xz2MIK8BONa2ZcyfMgJKQbXvhGp9A2gb/FZtbww28t0TUfeZBag78+SUNTpyc1aIyDdtooQRRL+MQb/riqlaCBSKUB2d5WWo0Af55InIff0fq6WXJu3UP9rzWZOMh/JYCaKUmghgn00FzJswgXxhUIa2nX+/MoRoSt15p6PuvDNClExlkedE5KM2LbMVZA6AzTYVMK9DAgN5qB2dpc/fHSbFVK18aDZyl8X+spCYWmcd5g0RmW5TylYQ/VuBT9hUwLwxEejrh+rYVfq4kmGklo75r5/G1AnvYYoikrNpha0gXwJwp00FzBuCQG/foAw7dgF6hRh6Ah0iXNQiNSSIRmH1FkZbQfTPpOkfM2GKi0BPb0mE0spQOpHeefhqUlx1RIxTY4JYvcvXVpCfAPhxRN7ZLX6w57AMemVo1yfTwaXVFFOpMUHOEBH9awNGiYIYYQqR6cDBw4dJemXQq0QVyFCupxTEcPyVUlxByrHa3x3I0AkE5w76JlytJApiOJIU5DCo4lMboF5tC4ToNCRYndkoiOG4URBAbdmO4h8fqtrDJcOhfkc2CmJILfOCdO1D/qpfGdKqnWwUxHAssy5I4Te3Qb24xZBW7WSjIIZjmWlBdu9F/urrDEnVVjYKYjieWRZEn3sUfnWTIanaykZBDMeTglAQw6mS5my8UehidLiCuKDqJSYFcYGdgrig6iUmBXGBnYK4oOolJgVxgZ2CuKDqJSYFcYGdgrig6iUmBXGBnYK4oOolJgVxgZ2CuKDqJSYFcYGdgrig6iUmBXGBnYK4oOolJgVxgZ2CuKDqJSYFcYG9FgSR5qmQWdOBmdMhs5ohMwdfEaU2voLC8jtGxMa9WIYzinuxqmcvlkw5ApjZXBJCi1ASo37MiCNdWHYr1Etby/5/CkJBRiWQ6hVk8oT/l0C0FHplGG/385HFVetQXPU4BRlGgG81GVWNwQypEWRcU7AqHF4dMHmCYS9Gzqbl0JKUS1xBDPHyECvhQ6z6MUMOkZoHzx30oZODREHKQ+UKYjjZklhBBs8VAhH0uUPzVMPWRc9GQShIpFkUtyAjXVGK1MgIhSkIBYkwfaKdg9heUYrU0JCFKQgFCTl1LE/SY7iiFKmhIQtTEAoScuqYCaJ/hanulI+Uft+vGhMFoSCR5m2lcxCZNxe5RRdHiu+7MAWhIJHmYCVB6i4+D3WnnhQpvu/CFISCRJqDlQTJLf5nyJxZkeL7LkxBKEikOUhBIuFLU2Hu5nUxGhTEBVUvMSmIC+wUxAVVLzEpiAvsFMQFVS8xKYgL7BTEBVUvMSmIC+wUxAVVLzEpiAvsFMQFVS8xKYgL7BTEBVUvMSmIC+y1LwgfuS03b/jAlKFNFMQQVPqzcQVxMUYUxAVVLzEpiAvsFMQFVS8xKYgL7BTEBVUvMSmIC+wUxAVVLzEpiAvstS7I/tXP4NXHX8LOhsnobJiEzsbJ2Km/Gybjrm8l93YVF2M3LCYFcQG51gW59fk+6E+5tOYb1fkY8QjzgIJQEHsCFKQ8M94HMZxLXEEMQaU/G1cQF2NEQVxQ9RKTgrjATkFcUPUSk4K4wE5BXFD1EpOCuMBOQVxQ9RKTgrjAPlyQfjRir0zBHpmC9373dEyaPclFtYnF5FUsXsWKNNl6t+zCyze0YC+mlMQ4IIeFOPvyJhw9Oxcpvu/CFISCRJqDnVsLWLu0p2wMChIJbdKFeYjlgjgFcUHVS0wK4gI7BXFB1UtMCuICe60LcuP/9OLuTf1l0XEvluGMyvKPeNa6ID9f14N1rw9QkGEEuBfL8I9DrQty2cpubH2rQEEoiKERw7LVsiAPbu7H0qd7RwTDQyzDOcNDrNq7zNvSmS/JsWNfkYKUIcBDLMM/DrW2gnQdVNArx0gPSQ3FwhXEcJJwBanuFaTj7SK2dxWwbU+xJIeWxCRREBNKAChI9QjSuvewDNsCKd48MPJhVKUpQEEoyKgE0n6I9cIbeWzoyGNbVxHb9hSMV4dROw6AgphQ4gqSur1Y7XuLWN82gPWteWz+3/KXaA2HtmI2CmJIkYdY6TnEWvVKP369fuRLs4ZDapSNghhhyvY5SOvzeTyxovyETHo3700b+nBnS/lX9BgOpVU2CmKIK8sryKaH+/HcyvJ7lZIUZMmTPXjk1fJbQgyH0TobBTFEllVB9u0q4uFlPTi4r/xl0aQEWfW3fvz6mWQOq3gfZJAAbxQa/HFYd2Mv2lryI+ZMQpD9fQrfub8b+l5G0okriCHxLK4g+rxDn39USkkIcvNzfbj9heTOO7iCcAUpO+cLA0DXjgJ2bCqgbWMe+vBqtORakNY9RXxnVTd6BszufI/WXtv/zxXEkFgtriD7Oovo2lHE7vZC6burvYj+HruJ6FoQfTlXX9b1lSiIIflqF6TnbVUSQK8Qu0vfRRzYPfoKMRoe14Kcf+t+dPfbSTtam23+PwUxpFWNggz0KrS1FNC+MV/xRNsQQdlsLgX5a0ceVz90MErzIpelIIYIq0mQgT6F51f2l84jRro8a9jtUbO5FGTNlgFc/+fyd/BHbVgMGeZNy+EXC8fHECk1IfjShrffLOKZO/qw61V3+5OGDrdLQSq90C2JKXfBCWNx6UmNSVSVVB3ZFkRLsf62Pux/K/q5hemIuRTkgVf6sSyhPVfl+vuzs8fhpPeOMUVRDfmyK0j7i3k8uaIXhcq3LWIfRJeCPN2ax88e9XMO0jyxDisueFfsvDwHzK4ga5f1oHNLModVSR1ibd9TxL/ec8DLnPr6Rxvw5fkNXup2WGk2Bdny9ACe/b2fO80uVxA9URbd243Xu5IV/9gjcrjuvHFoGGO1G8nhvI4tdPYE0Tf2Vv+yx+iud2yYhwRyLYiPE/XFn2rC2bPrXeDyHTN7gmxc3Y+ND/q70+xakJ37i/i3e7rRm0/mZuHHpo/BNeeM8z2RXdWfPUGe+F0vWl9I+Mx8yPB97gfj8O7pda4GtBRXX8nSV7Rcp5mT63DVp8dBf9doyp4g911z0NvhlZ5EX7x2PJomuD9Wv3J1N1p2ujsXOe49OVx5WlMty6GHK1uC5PsVbv9et9c/dpcsS+5S6Bdu3o8+B4da+mrVhfPGoqneveheBytrgrzVWsCDS/xtxZhyTA4LFzclOuaVXjRt25Bz547Fwrn1mH1kdf+EnEW/s7WCVHpflQW00Fnnfqoen/hS8vcK9DmJfjbddjWZOr4OHzwqhxObx+DEaTkcPaFmzzVGGtNsCbKno4j7f+7nTrMegdMvbcSM+X62YnTsK5Yk0S+M0+/IKneVa8bkOhw/JYfjp+ZK3/r+RsZTtgTp2a9w11V+zkF8HF5Vmtz6crB+3+6EBsHEBil95zK3QIyqf7YE0ThuvszPVoyTL2rA7AU1eTNt1FlWxRmyJ4jJixXiHtBpc3I467JkT87j7kNG4zkV5CoA/542sJXeeuiqrWd8qxHvO8HPuYerPmUk7ikist60r1YXvZVS3wDwO9PgSeZbc30P3nzN3U20oX2Zf+5YzF84Nsnusa74CBwnIq+bhrMV5FwAD5gGTzJfx8sFPLrc/f0QypHkqDqpa7yIGF/2tBXkIwD+6qTZMQR9flU/XnzIzX6liVPrsODiBkw9LvOXSWMYKW8h3haRSTa12wrSDKDDpoKk8+pn0beuj+/lzk2TBHMW1GPOKfXQ/2aqagJbRGSuTQ+sRlwppa+qJ3Ogb9OLYXk33NOHlx8LL8nYcQJ9leroOTnMmDeGYkQYi5QVfVJETrNpk5UgOrBSaheAqTaV+Mi7c3MB2zbksWNTHr0HKj9H0ThBMGVWDkfOrMORwXd9ozUaH91knXYE/iAiF9oUsZ4FSqmNAObZVOI7r96vpd+ouLutgP5ehcZ3Sekz8ai6khiTp/F2s+8xSqj+pSLybZu6wghyF4ALbCphXhJICYHLRWSZTVvCCPIVALfYVMK8JJASAu8Xkdds2hJGEH3+oc9DmEigmghsEpETbBtsLUhwov4ogE/bVsb8JOCRwHUisti2/rCCfA/AEtvKmJ8EPBI4S0Qesa0/rCCpvqNuC4H5a55Au4jMCNPLUIIEh1kvAJgfplKWIYGECdwkInqjrXWKIsj1AKyuKVu3jgVIIB4CF4vIHWFCRRHkwwCeBVBTv64SBiLLpJrAUyJyatgWhhYkOMzSD0/ph6iYSCCtBC4QkbvDNi6qIPqeiF5FjgnbAJYjAYcE7haRSLs+IgkSrCL6PESfjzCRQNoInCoiT0VpVGRBAkmeAfDJKA1hWRKImcByEVkUNWZcglwE4PaojWF5EoiJwB4AJ4vI5qjxYhEkWEX0idA/RW0Qy5NADAR+KiI/iSEO4hRkGoC1APTlXyYS8EVghYh8M67KYxMkWEVOAfAYAL4TJ64RYhwbAn8BcJqIxPZjlbEKEkjyVf02UJteMS8JxERgjohsjSlWKUzsggSS6OO/H8fZUMYigVEInCki+jGMWJMTQQJJ/hvAJbG2lsFIoDyB2E7Kh4d3JkggyWoA/8BRJQGHBNaKyDmu4jsVJJDkhwCuddUBxs00gSUicoVLAs4FCST5LIBVLjvC2JkjcImIOH95SCKCBJJ8DMCdAI7N3FCyw3ESaAHwVRHR385TYoIEkrwPwG95XuJ8XGu1gltEJNELP4kKEkiibyLqS8B6FzAftqrVqRxvv/SeqhtEZHm8YUePlrggh5qklNJbUrQkl47eTObIKAG96XBpIIf+d+LJmyBDRNHv19KifD7x3rPCNBPQq4VeNSLvyI3SSe+CDBFFb5m/nM+VRBnOmiird4VrMSI96BQXidQIMkSUMwGcBUB/6/dvMdU+gfsBPK4/IqJfJ5WalDpBhpJRSn0AgP5dRP3hq05TM20iN2QfgHuDe2PrROStyBEdBUi1IMNkadRbmQHMLPPRl4+Z0kdgO4BDn9ZD/xaRdelravkWVY0glYAGPw13SJxqYV/L7dwuIlqMqk81IUjVjwI7kFoCFCS1Q8OGpYEABUnDKLANqSVAQVI7NGxYGghQkDSMAtuQWgIUJLVDw4algQAFScMosA2pJUBBUjs0bFgaCFCQNIwC25BaAhQktUPDhqWBwP8BcpH8QYtDubAAAAAASUVORK5CYII='


def setPath(path: str = None):
    return '/'.join((path or __file__).split('\\'))


def setName(name: str):
    return sub(r'[\/:*"| !><?]', '', name)


def fileRW(path: str, name: str, mode: str = 'r', value=None):
    with open(f'{path}/{setName(name)}', mode, encoding='utf-8') as file:
        if '.json' in name:
            return dump(value, file, ensure_ascii=False) if value else loads(file.read())
        else:
            return file.write(value) if value else file.read()


def download(values, path: str, name: str, extension: str):
    try:
        with open(f'{path}/{setName(name)}.{extension}', 'wb') as file:
            file.write(values)
            file.flush()
    except FileNotFoundError:
        makedirs(path)
        download(values, path, name, extension)


def getConfig():
    try:
        return fileRW('./', 'config.json', 'r')
    except FileNotFoundError:
        config = {
            'app_name': '网易云音乐下载',
            'base64_icon': str(base64_icon, encoding='utf-8'),
            'path_icon': None,
            'path_app': setPath(dirname(__file__)),
            'path_download': './music',
            'max_download_number': 5
        }
        fileRW('./', 'config.json', 'w', config)
        return config


