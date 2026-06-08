from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

class Config(models.Model):
    class Tags(models.TextChoices):
        WM = 'WM'
        DE = 'DE'
        SHELL = 'Shell'
        TERMINAL = 'Terminal'
        NVIM_VIM = 'NVim/Vim'
        EMACS = 'Emacs'
        VSCODE = 'VSCode'
        BAR = "Bar"
        COMPOSITOR = 'Compositor'
        LAUNCHER = 'Launcher'
        FETCH = 'Fetch'
        ARCH = 'Arch'
        DEBIAN = 'Debian'
        NIXOS = 'NixOS'
        FEDORA = 'Fedora'
        MINT = 'Mint'
        GENTOO = 'Gentoo'
        UBUNTU = 'Ubuntu'

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(null=True, blank=True, upload_to='configs/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    tags = ArrayField(
        models.CharField(max_length=20, choices=Tags.choices),
        default=list,
        blank=True
    )
