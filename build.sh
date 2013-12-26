#!/bin/bash
set -e

RPMBUILD_DIR=`rpm --eval %{_topdir}`

pushd `dirname $0` > /dev/null
THRIFTRPM_DIR=$(pwd)
popd > /dev/null

cd $RPMBUILD_DIR/SOURCES
cp $THRIFTRPM_DIR/*.patch .
cd -

cd $RPMBUILD_DIR/SPECS
cp $THRIFTRPM_DIR/*.spec .
cd -

spectool -g -R $RPMBUILD_DIR/SPECS/thrift.spec
rpmbuild --clean -ba $RPMBUILD_DIR/SPECS/thrift.spec --nodeps
