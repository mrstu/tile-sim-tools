#!/usr/bin/perl
# Script to run the conversion tool vic2nc within SIMMA framework
#
# Author: Ted Bohn
# $Id: $
#-------------------------------------------------------------------------------

# Command-line arguments
$TOOLS_DIR = shift;
$PARAMS_TEMPLATE = shift;
$CONTROL_DIR = shift;
$InDir = shift;
$OutDir = shift;
$start_date = shift;
$end_date = shift;
$prefix = shift;

# Utility subroutines
require "$TOOLS_DIR/simma_util.pl";

# Parse & validate start/end dates
if ($start_date =~ /^(\d\d\d\d)-(\d\d)-(\d\d)$/) {
  ($start_year,$start_month,$start_day) = ($1,$2,$3);
}
else {
  die "$0: ERROR: start date must have format YYYY-MM-DD.\n";
}
if ($end_date =~ /^(\d\d\d\d)-(\d\d)-(\d\d)$/) {
  ($end_year,$end_month,$end_day) = ($1,$2,$3);
}
else {
  die "$0: ERROR: end date must have format YYYY-MM-DD.\n";
}

# Model parameters
open (PARAMS_TEMPLATE, $PARAMS_TEMPLATE) or die "$0: ERROR: cannot open parameter config file $PARAMS_TEMPLATE\n";
@params_template = <PARAMS_TEMPLATE>;
close (PARAMS_TEMPLATE);

# Check for directories; create if necessary
if (!-d $InDir) {
  die "$0: ERROR: directory $InDir not found\n";
}
foreach $dir ($OutDir) {
  $status = &make_dir($dir);
}

# Unique identifier for this job
$JOB_ID = `date +%y%m%d-%H%M%S`;
if ($JOB_ID =~ /(\S+)/) {
  $JOB_ID = $1;
}

#-------------------------------------------------------------------------------
# Model execution
#-------------------------------------------------------------------------------

# Create input file
$status = &make_dir($CONTROL_DIR);
$controlfile = "$CONTROL_DIR/inp.$JOB_ID";
open (CONTROLFILE, ">$controlfile") or die "$0: ERROR: cannot open controlfile $controlfile\n";
foreach (@params_template) {
  s/<FORCE_START_YEAR>/$start_year/g;
  s/<FORCE_START_MONTH>/$start_month/g;
  s/<FORCE_START_DAY>/$start_day/g;
  s/<FORCE_END_YEAR>/$end_year/g;
  s/<FORCE_END_MONTH>/$end_month/g;
  s/<FORCE_END_DAY>/$end_day/g;
  print CONTROLFILE $_;
}
close(CONTROLFILE);

# Run the model
#$cmd = "$TOOLS_DIR/vic2nc -i $InDir -p $prefix -m $controlfile -o $OutDir/$prefix -c -t m";
$cmd = "$TOOLS_DIR/vic2nc -i $InDir -p $prefix -m $controlfile -o $OutDir/$prefix -t m";
print "$cmd\n";
#(system($cmd)==0) or die "$0: ERROR in $cmd: $?\n";
system($cmd);  
#FIXED: vic2nc was alway returning an error signal.  
#Added "return 0;" to vic2nc.c
#Added passing of return value from vic2nc through run_vic2nc.pl to parent script.
#The exit code from vic2nc get multiplied by 256 so have to right-shift the bits using the >> bitwise operator with 8 bits
#http://perlmaven.com/how-to-exit-from-perl-script
$pexit=$?>>8;
exit $pexit;
