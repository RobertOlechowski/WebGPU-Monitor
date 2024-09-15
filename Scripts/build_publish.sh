clear

# docker login ghcr.io -u robertolechowski
# github login

github_repo="ghcr.io/robertolechowski"
image_name="webgpu-monitor"


#if ! git diff-index --quiet HEAD --; then
#    echo "The repository has uncommitted changes. Aborting script."
#    exit 1
#fi

version=$(python3 buildUtls.py get_ver)
build_time=$(python3 buildUtls.py time)

echo
echo
echo 'Build and docker image and increase version'
echo Image        : $image_name
echo Version      : $version
echo Build time   : $build_time
echo
echo

echo "Repository is clean. Adding tag."
git tag -a "$version" -m "New release tag $version"

echo
echo '=== GIT PUSH ==='
echo
git push origin "$version"
git push origin main

#=======================================

echo
echo '=== BUILD ==='
echo
docker build --build-arg BUILD_VERSION=${version}  --build-arg BUILD_TIME=${build_time}  -t $image_name:$version ../.
echo
docker tag $image_name:$version $image_name:latest

echo
echo '=== PUSH to GitHub ==='
echo
docker tag $image_name:$version $github_repo/$image_name:latest
docker tag $image_name:$version $github_repo/$image_name:$version
docker push $github_repo/$image_name:$version
docker push $github_repo/$image_name:latest

echo
echo '=== Increment version number ==='
echo
version=$(python3 buildUtls.py inc_ver)

