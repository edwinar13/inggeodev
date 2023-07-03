from flask import current_app as app
from flask_assets import Bundle


def compileStaticAssets(assets):
    assets.auto_build = True
    assets.debug = False
    common_less_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.css',
        extra={'rel': 'stylesheet/less'}
    )
    BPhome_less_bundle = Bundle(
        'home_bp/less/BPhome.less',
        filters='less,cssmin',
        output='dist/css/BPhome.css',
        extra={'rel': 'stylesheet/less'}
    )
    BPapplication_less_bundle = Bundle(
        'profile_bp/less/BPapplication.less',
        filters='less,cssmin',
        output='dist/css/BPapplication.css',
        extra={'rel': 'stylesheet/less'}
    )
    BPauthentication_less_bundle = Bundle(
        'products_bp/less/BPauthentication.less',
        filters='less,cssmin',
        output='dist/css/BPauthentication.css',
        extra={'rel': 'stylesheet/less'}
    )
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('BPhome_less_bundle', BPhome_less_bundle)
    assets.register('BPapplication_less_bundle', BPapplication_less_bundle)
    assets.register('BPauthentication_less_bundle', BPauthentication_less_bundle)
    if app.config['FLASK_ENV'] == 'development':
        common_less_bundle.build()
        BPhome_less_bundle.build()
        BPapplication_less_bundle.build()
        BPauthentication_less_bundle.build()
    return assets