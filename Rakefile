require "yast/rake"
require "fileutils"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

# create pre-commit hook if missing
if !File.exist? ".git/hooks/pre-commit"
  FileUtils.ln_s "../../git-hooks/pre-commit.sh", ".git/hooks/pre-commit"
end

# check also the syntax of the XML files
task :"check:syntax" do
  sh "make -C control check"
end
