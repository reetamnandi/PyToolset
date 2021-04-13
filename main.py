import filecmp
import difflib
import click


@click.group()
@click.version_option("1.0.0")
@click.pass_context
def main(ctx):
    """A CLI toolset with handy commands"""
    pass


@main.command(help="Compares 2 files and produces `git diff` like result")
@click.option('--prev', '-p', type=click.Path(True, True, False, False, True, True), default='./file1.txt', show_default=True, prompt=True, help="Fully Qualified Path to previous version of File", required=True)
@click.option('--curr', '-c', type=click.Path(True, True, False, False, True, True), default='./file2.txt', show_default=True, prompt=True, help="Fully Qualified Path to current version of File", required=True)
@click.option('--out', '-o', type=click.Path(True, True, False, True, False, True), default='./diff.txt', show_default=True, prompt=True, help="Fully Qualified Path to Diff Output File", required=True)
@click.pass_context
def compare(ctx, prev, curr, out):
    status = filecmp.cmp(prev, curr)

    if(status):
        print("\nFiles are Equal!\n")
    else:
        file1 = open(prev, "r")
        file2 = open(curr, "r")
        diff = difflib.unified_diff(
            file1.readlines(), file2.readlines(), fromfile=prev, tofile=curr)
        diffFile = open(out, "w")
        diffFile.writelines(diff)
        diffFile.close()
        file2.close()
        file1.close()
        print(
            f'\nFiles are Unequal, Check {out} for detailed diff breakdown\n')


if __name__ == "__main__":
    main()
