# shell.nix
let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {

  buildInputs = [
    pkgs.uv
    pkgs.python313
    pkgs.python313Packages.python-lsp-server
    
  ];
}
