{ pkgs }: {
    deps = [
      pkgs.python311Packages.flask
      pkgs.cowsay
    ];
}